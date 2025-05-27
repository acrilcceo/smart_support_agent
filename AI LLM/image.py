from together import Together

client = Together()
response = client.images.generate(
    prompt="Cats eating popcorn",
    model="black-forest-labs/FLUX.1-dev",
    steps=10,
    n=4
)
print(response.data[0].b64_json)