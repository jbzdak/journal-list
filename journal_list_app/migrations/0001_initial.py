# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Journal'
        db.create_table('journal_list_app_journal', (
            ('issn', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(db_index=True)),
            ('pts', self.gf('django.db.models.fields.PositiveSmallIntegerField')(db_index=True)),
            ('cathegory', self.gf('django.db.models.fields.PositiveSmallIntegerField')(db_index=True)),
        ))
        db.send_create_signal('journal_list_app', ['Journal'])


    def backwards(self, orm):
        # Deleting model 'Journal'
        db.delete_table('journal_list_app_journal')


    models = {
        'journal_list_app.journal': {
            'Meta': {'object_name': 'Journal'},
            'cathegory': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True'}),
            'issn': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'pts': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['journal_list_app']