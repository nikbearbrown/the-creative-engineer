# Adding a key, securely

Most of the time you need **no key** — when you work in Cowork/Claude, the agent
is the model and does everything on your subscription. A key is only for optional
extras (e.g. spoken audio on flashcards, via ElevenLabs) or if you later run the
scripts yourself unattended.

When you *do* need one, here is the safe way. **Your key stays on your computer
and never goes through this chat.**

---

## The secure way (recommended)

1. Tell the agent which key you have — e.g. *"I have an ElevenLabs key to add."*
2. The agent creates the private `.env` file for you (from the template) and
   **opens it** in your text editor.
3. You paste your key after the `=` on its line, and **save the file**. Example:
   ```
   ELEVENLABS_API_KEY=el_xxxxxxxxxxxxxxxxxxxx
   ```
4. The agent confirms the key is set — **without ever displaying it**.

That's it. Your key now lives only in `.env` on your computer. `.env` is
*gitignored*, so it is never uploaded, never committed, never shared when you
publish the book — and it never appears in this chat.

## The quick way (less private)

If you'd rather, paste the key into the chat and the agent will save it to `.env`
for you. **Trade-off:** the key then passes through the chat (to Claude's servers)
and stays in your chat history. Fine for a low-stakes key; use the secure way for
anything sensitive.

## Why `.env`?

`.env` is the one private file where keys live. Git is told to ignore it
automatically, so publishing or sharing the book never exposes it. The agent
reads keys from it to run a tool, but never prints them back.

## Removing or changing a key

Just ask — *"remove my ElevenLabs key"* or *"update my key."* The agent opens
`.env`, you replace or clear that line, and save. Nothing else to do.

---

*Reminder: the only key most people ever touch is the optional audio one. The
book — chapters, figures, quizzes, Canvas export, fact-checking — all works with
no key at all.*
