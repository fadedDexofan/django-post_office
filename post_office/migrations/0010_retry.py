from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_office', '0009_requeued_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='emails',
            field=models.ManyToManyField(related_name='attachments', to='post_office.Email', verbose_name='Emails'),
        ),
        migrations.AlterField(
            model_name='email',
            name='expires_at',
            field=models.DateTimeField(blank=True, help_text="Email won't be sent after this timestamp", null=True, verbose_name='Expires'),
        ),
        migrations.AlterField(
            model_name='email',
            name='scheduled_time',
            field=models.DateTimeField(blank=True, db_index=True, help_text='The scheduled sending time', null=True, verbose_name='Scheduled Time'),
        ),
    ]
