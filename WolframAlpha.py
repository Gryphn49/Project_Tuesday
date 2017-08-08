import wolframalpha

input = raw_input("Question: ")
app_id = "G58JY9-WQ963T9EQV"

client = wolframalpha.Client(app_id)

result = client.query(input)
answer = next(result.results).text

print answer
