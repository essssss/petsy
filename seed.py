from models import Pet, db
from app import app


# Create all tables
db.drop_all()
db.create_all()

frisky = Pet(
    name="Frisky",
    species="cat",
    photo_url="https://images.squarespace-cdn.com/content/5259cce9e4b0b7382f189a32/42c51b0d-5ace-4c4a-a298-54611518a24e/petsy-1.jpg?content-type=image%2Fjpeg",
    age=2,
    notes="Frisky is a quiet and reserved kitty. Best in a home with no pets or children!",
)
maynard = Pet(
    name="Maynard",
    species="cat",
    photo_url="https://images.squarespace-cdn.com/content/5259cce9e4b0b7382f189a32/48a50a61-3343-4c63-9023-3c969ad8252b/petsy-3.jpg?content-type=image%2Fjpeg",
    age=1,
    notes="Maynard loves to play and frolic. This social kitty would be great in a home with dogs or kids!",
    available=False,
)
felicia = Pet(
    name="Felicia",
    species="cat",
    photo_url="https://images.squarespace-cdn.com/content/5259cce9e4b0b7382f189a32/ea65fbcf-b05c-40cf-aba9-fad325dd69e6/petsy-2.jpg?content-type=image%2Fjpeg",
    age=8,
    notes="FElicia is an older kitty who loves to snuggle.",
)
juan = Pet(
    name="Juan",
    species="dog",
    photo_url="https://images.squarespace-cdn.com/content/5259cce9e4b0b7382f189a32/bcef753c-e8b4-4ffb-9e55-2242f6eea5f7/petsy-6.jpg?content-type=image%2Fjpeg",
    age=4,
    notes="Juan is a calm doggy. He is content to run around outside or sit on the couch all day.",
)
marisol = Pet(
    name="Marisol",
    species="dog",
    photo_url="https://images.squarespace-cdn.com/content/5259cce9e4b0b7382f189a32/3473b6ec-0483-403c-90c6-bdb1eba0037f/petsy-5.jpg?content-type=image%2Fjpeg",
    age=2,
    notes="She's a real handful!",
    available=False,
)
bruce = Pet(
    name="Bruce",
    species="dog",
    photo_url="https://images.squarespace-cdn.com/content/5259cce9e4b0b7382f189a32/4cd762dd-e7af-4098-bf71-575936f4ebb3/petsy-4.jpg?content-type=image%2Fjpeg",
    age=0,
    notes="Bruce is a sweet lil pup. Just about to turn 6 months!",
)
norman = Pet(name="Norman", species="dog", age=9, available=False)
piggie = Pet(
    name="Piggie",
    species="porcupine",
    photo_url="https://images.squarespace-cdn.com/content/5259cce9e4b0b7382f189a32/9f72945d-1202-4e7d-bedc-2fc361b0cb44/petsy-7.jpg?content-type=image%2Fjpeg",
    age=2,
    notes="Piggie is Pokey!",
    available=False,
)
spike = Pet(
    name="Spike",
    species="porcupine",
    photo_url="https://images.squarespace-cdn.com/content/5259cce9e4b0b7382f189a32/fad79972-a40e-426d-8d7f-ec3efdba8942/petsy-8.jpg?content-type=image%2Fjpeg",
    age=1,
    notes="We had to have a porcupine named Spike. It's in our contract.",
)

db.session.add_all(
    [frisky, maynard, felicia, juan, marisol, bruce, norman, piggie, spike]
)
db.session.commit()
