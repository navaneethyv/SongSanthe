# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Content'
        db.create_table(u'content_content', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'content', ['Content'])


    def backwards(self, orm):
        # Deleting model 'Content'
        db.delete_table(u'content_content')


    models = {
        u'content.content': {
            'Meta': {'object_name': 'Content'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['content']