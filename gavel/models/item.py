from gavel.models import db
import gavel.crowd_bt as crowd_bt
from sqlalchemy.orm.exc import NoResultFound

view_table = db.Table('view',
    db.Column('item_id', db.Integer, db.ForeignKey('item.id')),
    db.Column('annotator_id', db.Integer, db.ForeignKey('annotator.id'))
)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.Text, nullable=False, unique=True)                      # team name
    location = db.Column(db.Text, nullable=False, unique=True)                  # Seat alloted
    secret_key = db.Coloumn(db.Text, nullable=False, unique=True)               # Alloted secret key
    title = db.Column(db.Text, default="", nullable=False)                      # Project Title
    description = db.Column(db.Text, default="", nullable=False)                # Project description
    demo_link = db.Column(db.Text, default="", nullable=False)                  # Project demo video
    git_link = db.Column(db.Text, default="", nullable=False)                   # Github repo link for the project
    inspiration = db.Column(db.Text, default="", nullable=False)                # Project Inspiration
    how_built = db.Column(db.Text, default="", nullable=False)                  # Project build description
    challenges = db.Column(db.Text, default="", nullable=False)                 # Challenges faced
    accomplishments = db.Column(db.Text, default="", nullable=False)            # Accomplishments
    learned = db.Column(db.Text, default="", nullable=False)                    # What learned
    next = db.Column(db.Text, default="", nullable=False)                       # What's next
    built_with = db.Column(db.Text, default="", nullable=False)                 # Technologies used
    active = db.Column(db.Boolean, default=True, nullable=False)
    viewed = db.relationship('Annotator', secondary=view_table)
    prioritized = db.Column(db.Boolean, default=False, nullable=False)
    submitted  = db.Column(db.Boolean, default=False, nullable=False)           # Project Submitted

    mu = db.Column(db.Float)
    sigma_sq = db.Column(db.Float)

    def __init__(self, name, location, secret_key):
        self.name = name
        self.location = location
        self.secret_key = secret_key
        self.mu = crowd_bt.MU_PRIOR
        self.sigma_sq = crowd_bt.SIGMA_SQ_PRIOR

    @classmethod
    def by_id(cls, uid):
        if uid is None:
            return None
        try:
            item = cls.query.get(uid)
        except NoResultFound:
            item = None
        return item
