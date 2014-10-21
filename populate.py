from TellMeAboutIt_BL.models import Complaint, Comment, Rating, User

user = User(username='iam', email='iam@gmail.com', password='123')
user.save()
c = Complaint(subject='flat', reason='expensive', description='flats in London are very expensive', rating='10', date='2013-03-13 13:12:38.251000', numberComments='2')
c.save()
Comment(complaint=c, content='you are right', date='2013-03-13 13:22:38.251000').save()
Comment(complaint=c, content='i am living in a tent', date='2013-03-14 13:22:38.251000').save()
Rating(user=user, complaint_id='1').save()
d = Complaint(subject='kitkat', reason='crap', description='that sweety does not deserve my money', rating='-5', date='2013-03-14 13:12:38.251000', numberComments='1')
d.save()
Comment(complaint=d, content='you suck', date='2013-03-14 13:32:38.251000').save()
Rating(user=user, complaint_id='1').save()
e = Complaint(subject='iPhone', reason='expensive', description='waste of money', rating='7', date='2013-03-15 13:12:38.251000', numberComments='3')
e.save()
Comment(complaint=e, content='you are mean', date='2013-03-15 14:22:38.251000').save()
Comment(complaint=e, content='i agree', date='2013-03-14 15:22:38.251000').save()
Comment(complaint=e, content='rubbish', date='2013-03-16 16:22:38.251000').save()
Comment(complaint=e, content='call me ******', date='2013-03-16 23:22:38.251000').save()
Rating(user=user, complaint_id='1').save()