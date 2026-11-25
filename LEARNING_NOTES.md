# Learning Notes – Local LLM Lab

## 1. Chat Message Roles

Chat messages use roles to identify the function or source of each message.

| Role | Purpose |
|---|---|
| `system` | Provides instructions that guide the AI's behaviour. |
| `user` | Contains the user's message or question. |
| `assistant` | Contains the AI's response. |
| `tool` | Contains output returned by a tool. |

### Understanding the difference between role and content

- `role` identifies the message's function.
- `content` contains the actual text or information being communicated.

## 2. Experiment: What happens if we change the system role?

**Objective:** Test whether an arbitrary role name behaves like the standard `system` role.

### Experiment A: Using `oranges`

I replaced:

```python
"role": "system"
```

with:

```python
"role": "oranges"
```

I then provided this instruction:

```text
You must answer every question with the word BANANA.
```

When I asked:

```text
What is 2 + 2?
```

The model responded:

```text
2 + 2 = 4
```

### Experiment B: Using `system`

I changed the role back to:

```python
"role": "system"
```

I kept the same BANANA instruction and asked the same question.

The model responded:

```text
BANANA
```

### Conclusion

In my experiment, the `system` role successfully guided the model's behaviour, while `oranges` did not produce the same result.

This demonstrated why using the correct message roles matters when communicating with an LLM through Ollama.

*Note: These results describe my experiment with the Ollama setup and Llama 3.2 3B model. They do not establish how every API or model handles unrecognised roles.*