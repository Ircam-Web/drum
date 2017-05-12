from modeltranslation.translator import translator, register, TranslationOptions

from drum.links.models import *

@register(Link)
class LinkTranslationOptions(TranslationOptions):
    fields = ()
