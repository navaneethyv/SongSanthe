# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Tag', fields ['content']
        db.delete_unique(u'content_tag', ['content_id'])

        # Removing unique constraint on 'Upvoters', fields ['content']
        db.delete_unique(u'content_upvoters', ['content_id'])

        # Removing unique constraint on 'Downvoters', fields ['content']
        db.delete_unique(u'content_downvoters', ['content_id'])


        # Changing field 'Downvoters.content'
        db.alter_column(u'content_downvoters', 'content_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Content']))

        # Changing field 'Upvoters.content'
        db.alter_column(u'content_upvoters', 'content_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Content']))

        # Changing field 'Tag.content'
        db.alter_column(u'content_tag', 'content_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Content']))

    def backwards(self, orm):

        # Changing field 'Downvoters.content'
        db.alter_column(u'content_downvoters', 'content_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['content.Content'], unique=True))
        # Adding unique constraint on 'Downvoters', fields ['content']
        db.create_unique(u'content_downvoters', ['content_id'])


        # Changing field 'Upvoters.content'
        db.alter_column(u'content_upvoters', 'content_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['content.Content'], unique=True))
        # Adding unique constraint on 'Upvoters', fields ['content']
        db.create_unique(u'content_upvoters', ['content_id'])


        # Changing field 'Tag.content'
        db.alter_column(u'content_tag', 'content_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['content.Content'], unique=True))
        # Adding unique constraint on 'Tag', fields ['content']
        db.create_unique(u'content_tag', ['content_id'])


    models = {
        u'actstream.action': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'Action'},
            'action_object_content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'action_object'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'action_object_object_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'actor_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actor'", 'to': u"orm['contenttypes.ContentType']"}),
            'actor_object_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'data': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'target_content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'target'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'target_object_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'verb': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'content.content': {
            'Meta': {'object_name': 'Content'},
            'content_type': ('django.db.models.fields.TextField', [], {'default': "'LYRICS'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_stamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content_uploader'", 'to': u"orm['auth.User']"}),
            'user_content_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'content.downvoters': {
            'Meta': {'object_name': 'Downvoters'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.Content']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'downvoter'", 'to': u"orm['auth.User']"})
        },
        u'content.lyrics': {
            'Meta': {'object_name': 'Lyrics'},
            'content': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['content.Content']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lyrics_content': ('django.db.models.fields.TextField', [], {}),
            'lyrics_title': ('django.db.models.fields.TextField', [], {})
        },
        u'content.music': {
            'Meta': {'object_name': 'Music'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'content': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['content.Content']", 'unique': 'True'}),
            'filepath': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'content.tag': {
            'Meta': {'object_name': 'Tag'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.Content']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_name': ('django.db.models.fields.TextField', [], {})
        },
        u'content.upvoters': {
            'Meta': {'object_name': 'Upvoters'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.Content']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'upvoter'", 'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['content']