from rest_framework import serializers
from quiz.models import Questions, Answer


class QuestionsSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Questions
        fields = [
            'id',
            'subject',
            'topic',
            'technique',
            'difficulty',
            'question',
            'difficulty',
            'date_created',
            'is_active'
        ]


class AnswerSerializers(serializers.ModelSerializer):

    question = serializers.ReadOnlyField(source='question_number.question')

    class Meta:
        model = Answer
        fields = [
            'id',
            'question',
            'question_number',
            'answer_text',
            'is_right'
        ]
