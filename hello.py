import anthropic

# yes That's it. This is all it takes.
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Analyze this contract."}]
)
print(message.content); 