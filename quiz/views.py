from queue import Empty
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ViewSet
from quiz.serializers import QuestionsSerializers, AnswerSerializers
from quiz.models import Questions, Answer
from rest_framework.response import Response

# Create your views here.


class Question(ViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializers
    lookup_field = 'subject'


    def list(self, request):
        serializer = QuestionsSerializers(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, subject=None):
        sub = Questions.objects.filter(subject=subject.title())
        serializer = QuestionsSerializers(sub, many=True)
        return Response(serializer.data)


class Answers(ListAPIView):
    serializer_class = AnswerSerializers

    def get_queryset(self):
        question = self.kwargs['question']
        subject = self.kwargs['subject'].title()

        if len(Questions.objects.filter(subject=subject , question = question)) == 1:
            return Answer.objects.filter(question_number__question=question)
