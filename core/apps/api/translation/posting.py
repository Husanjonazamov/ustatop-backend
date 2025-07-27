from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import PostingModel


@register(PostingModel)
class PostingTranslation(TranslationOptions):
    fields = []
