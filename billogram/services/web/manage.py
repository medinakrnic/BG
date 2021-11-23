from flask.cli import FlaskGroup

from project import app, db
from project.models import DiscountCodes, Users

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(
        Users(
            username="maddierobson",
            name="Maddie Robson",
            email="maddierobson@gmail.com",
        )
    )
    db.session.add(
        Users(
            username="rickbillson", name="Rick Billson", email="rickbillson@gmail.com"
        )
    )
    db.session.add(
        Users(username="bobolsson", name="Bob Olsson", email="bobolsson@gmail.com")
    )
    db.session.add(
        Users(username="tinasmith", name="Tina Smith", email="tinasmith@gmail.com")
    )
    db.session.add(
        Users(username="nickday", name="Nick Day", email="nickday@gmail.com")
    )
    db.session.add(DiscountCodes(discount_code="BRAND40-GSXQQ", discount_value=40))
    db.session.add(DiscountCodes(discount_code="BRAND40-DBF6Z", discount_value=40))
    db.session.add(DiscountCodes(discount_code="BRAND40-NS9SH", discount_value=40))
    db.session.add(DiscountCodes(discount_code="BRAND40-SPM1A", discount_value=40))
    db.session.add(DiscountCodes(discount_code="BRAND40-LY20A", discount_value=40))

    db.session.commit()


if __name__ == "__main__":
    cli()
