# Generated by Django 4.0.3 on 2022-04-16 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gspt_test', '0003_person_remove_student_adviser_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='adviser_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='gspt_test.person'),
        ),
    ]