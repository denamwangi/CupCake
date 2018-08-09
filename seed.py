from model import db, connect_to_db, User, Cupcake, UserCupcake, Role


def load_users():
    """Add sample users to the DB"""

    for user in ["Katie", "Dena", "Maya", "Kiko", "Carol"]:
        new_user = User(name=user,
                        email="{user}@gmail.com".format(user=user.lower()),
                        password=user)
        db.session.add(new_user)

    db.session.commit()
    print "users added"


def load_roles():

    for role in ["sender", "recipient"]:
        new_role = Role(role=role)
        db.session.add(new_role)

    db.session.commit()
    print "roles added"


# TODO this is not done!!
def load_cupcakes():
    """Add sample cupcakes to the DB"""

    katie, dena, maya, kiko, carol = User.query.all()
    cupcake = Cupcake(reason="being awesome",
                      sender=katie,
                      recipients=[dena, carol])
    db.session.add(cupcake)
    db.session.commit()
    # UserCupcake.mark_sender(cupcake, katie)
    # UserCupcake.mark_recipients(cupcake, [dena, carol])

    db.session.commit()
    print "cupcakes added"


if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)

    db.create_all()
    load_users()
    load_roles()
    load_cupcakes()
