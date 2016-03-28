# -*- coding: utf-8 -*-
from django.db import models
import urllib2

class Domain(models.Model):
	name = models.URLField(max_length = 255, verbose_name = u"Назва")
	is_private = models.BooleanField(default = False, verbose_name=u"Чи приватиний домен?")

	class Meta:
		verbose_name = u'Домен'
		verbose_name_plural = u'Домени'

	def __unicode__(self):
		return u'%s' % self.name

	def is_https(self):
		if self.name[:5] == "https":
			return True
		else:
			return False

	def is_valid_address(self):
		try:
			urllib2.urlopen(self.name)
			return True
		except:
			return False