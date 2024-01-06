from django.shortcuts import render,get_object_or_404,redirect,resolve_url
from django.http import HttpResponse
from .models import Question, Answer, Comment
from django.utils import timezone
from .forms import QuestionForm, AnswerForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count

# Create your views here.

def main(request):
    return render(request, 'main.html')

def index(request):
    page=request.GET.get('page','1')
    kw=request.GET.get('kw','')
    so=request.GET.get('so','recent')

    if so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  
        question_list = Question.objects.order_by('-create_date')

    if kw:
        question_list=question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        ).distinct()
    paginator=Paginator(question_list,10)
    page_obj=paginator.get_page(page)

    context={'question_list':page_obj, 'page':page, 'kw':kw, 'so':so}
    return render(request, 'community/question_list.html', context)

def detail(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    question = Question.objects.get(id=question_id)
    context={'question':question}
    return render(request, 'community/question_detail.html', context)

# 질문 게시판 관련
@login_required(login_url='common:login')
def question_create(request):
    if request.method =='POST':
        form=QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question=form.save(commit=False)
            question.author=request.user
            question.create_date=timezone.now()
            question.save()
            return redirect('community:index')
    else:
        form=QuestionForm()
    return render(request, 'community/question_form.html', {'form': form})

@login_required(login_url='common:login')
def question_modify(request,question_id):
    question=get_object_or_404(Question,pk=question_id)

    if request.user != question.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('community:detail', question_id=question.id)

    if request.method =='POST':
        form=QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question=form.save(commit=False)
            question.author=request.user
            question.modify_date=timezone.now()
            question.save()
            return redirect('community:detail',question_id=question.id)
    else:
        form=QuestionForm(instance=question)
    context={'form':form}
    return render(request, 'community/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request,question_id):
    question=get_object_or_404(Question,pk=question_id)

    if request.user != question.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('community:detail', question_id=question.id)
    question.delete()
    return redirect('community:index')

# 질문에 대한 답변게시판 관련
@login_required(login_url='common:login')
def answer_create(request,question_id):
    question=get_object_or_404(Question,pk=question_id)

    if request.method =='POST':
        form=AnswerForm(request.POST)
        if form.is_valid():
            answer=form.save(commit=False)
            answer.author=request.user
            answer.create_date=timezone.now()
            answer.question=question
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('community:detail',question_id=question.id),answer.id))
    else:
        form=AnswerForm()
    context={'question':question, 'form':form}
    return render(request, 'community/question_detail.html', context)

@login_required(login_url='common:login')
def answer_modify(request,answer_id):
    answer=get_object_or_404(Answer,pk=answer_id)

    if request.user != answer.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('community:detail', question_id=answer.question.id)

    if request.method =='POST':
        form=AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer=form.save(commit=False)
            answer.author=request.user
            answer.modify_date=timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('community:detail',question_id=answer.question.id),answer.id))
    else:
        form=AnswerForm(instance=answer)
    context={'answer':answer,'form':form}
    return render(request, 'community/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request,answer_id):
    answer=get_object_or_404(Answer,pk=answer_id)

    if request.user != answer.author:
        messages.error(request, '삭제 권한이 없습니다.')
    else:
        answer.delete()
    return redirect('community:detail', question_id=answer.question.id)

# 질문게시글 댓글 기능
@login_required(login_url='common:login')
def comment_create_question(request,question_id):
    question=get_object_or_404(Question,pk=question_id)

    if request.method =='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.create_date=timezone.now()
            comment.question=question
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('community:detail',question_id=comment.question.id),comment.id))
    else:
        form=CommentForm()
    context={'form':form}
    return render(request, 'community/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_question(request,comment_id):
    comment=get_object_or_404(Comment,pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('community:detail', question_id=comment.question.id)

    if request.method =='POST':
        form=CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.modify_date=timezone.now()
            comment.save()

            return redirect('{}#comment_{}'.format(
                resolve_url('community:detail',question_id=comment.question.id),comment.id))
    else:
        form=CommentForm(instance=comment)
    context={'form':form}
    return render(request, 'community/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_question(request,comment_id):
    comment=get_object_or_404(Comment,pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '삭제 권한이 없습니다.')
    else:
        comment.delete()
    return redirect('community:detail', question_id=comment.question.id)

# 답변게시글 댓글 기능
@login_required(login_url='common:login')
def comment_create_answer(request,answer_id):
    answer=get_object_or_404(Answer,pk=answer_id)

    if request.method =='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.create_date=timezone.now()
            comment.answer=answer
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('community:detail',question_id=comment.answer.question.id),comment.id))
    else:
        form=CommentForm()
    context={'form':form}
    return render(request,'community/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_answer(request,comment_id):
    comment=get_object_or_404(Comment,pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('community:detail', question_id=comment.answer.question.id)

    if request.method =='POST':
        form=CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.modify_date=timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('community:detail',question_id=comment.answer.question.id),comment.id))
    else:
        form=CommentForm(instance=comment)
    context={'form':form}
    return render(request, 'community/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_answer(request,comment_id):
    comment=get_object_or_404(Comment,pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('community:detail', question_id=comment.answer.question.id)
    else:
        comment.delete()
    return redirect('community:detail', question_id=comment.answer.question.id)