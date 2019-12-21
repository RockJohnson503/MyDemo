# encoding: utf-8

"""
File: comment_block.py
Author: Rock Johnson
"""
from django import template

from comment.models import Comment
from comment.forms import CommentForm


register = template.Library()

@register.inclusion_tag('comment/block.html')
def comment_block(target):
    return {
        'target': target,
        'comment_form': CommentForm(),
        'comment_list': Comment.get_by_target(target),
    }
