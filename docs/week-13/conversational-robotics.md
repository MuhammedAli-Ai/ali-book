---
sidebar_position: 1
title: Conversational Robotics
---

# Conversational Robotics

Traditional voice assistants (Siri/Alexa) are scripted. **Conversational Robotics** uses Large Language Models (LLMs) to understand intent and context.

## The Pipeline

1.  **STT (Speech-to-Text)**: Convert audio to text.
    - *Tool*: OpenAI Whisper (runs fast on GPU).
2.  **LLM (Brain)**: Understand text and decide action.
    - *Tool*: GPT-4o, Claude 3.5 Sonnet, or Llama 3 (local).
3.  **TTS (Text-to-Speech)**: Convert text reply to audio.
    - *Tool*: ElevenLabs, Coqui TTS.

## JSON Mode for Action

LLMs are great at talking, but how do they control motors? We force the LLM to output **JSON**.

**System Prompt**:
> You are a robot assistant. If asked to move, output JSON: `{"action": "move", "x": 1.0, "y": 0.0}`. Do not chatter.

**User**: "Go forward a meter."

**LLM Output**: `{"action": "move", "x": 1.0, "y": 0.0}`

A Python script parses this JSON and calls the ROS 2 Action Server.
