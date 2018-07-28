#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms

from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"


class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item
        fields = ('text', )
        widgets = {
            'text':
            forms.fields.TextInput(
                attrs={
                    'placeholder': 'Enter a to-do item',
                    'class': 'form-control input-lg',
                    'id': 'id-text',
                })
        }
        error_messages = {'text': {'required': EMPTY_ITEM_ERROR}}


if __name__ == '__main__':
    pass