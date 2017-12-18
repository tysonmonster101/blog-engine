from django import forms

from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = self.user
        post = super(PostForm, self).save(commit=False)
        post.user = user

        if commit:
            post.save()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )

    def __init__(self, *args, **kwargs):
        self.post = kwargs.pop('post', None)
        self.user = kwargs.pop('user', None)
        super(CommentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = self.user
        post = self.post
        comment = super(CommentForm, self).save(commit=False)
        comment.user = user
        comment.post = post
        if commit:
            comment.save()
