---
sidebar_position: 2
title: Multimodal Interaction
---

# Vision-Language-Action (VLA)

The frontier of Physical AI is **VLA Models**. These models accept both text and images as input and output actions directly.

## Understanding the Scene

Instead of just hearing "Pick up the apple," the robot *sees* the table with an apple and a banana.

**Prompt**: (Image Included) "Pick up the red fruit."
**VLA Output**: `{"action": "pick", "object_bbox": [100, 200, 50, 50]}`

## Capstone Project: The Autonomous Butler

In this final project, you will build a pipeline:

1.  User says: "Bring me the soda."
2.  **Whisper** converts to text.
3.  **VLM (Vision Language Model)** looks at camera feed to find "soda".
4.  **Nav2** plans path to the soda.
5.  **MoveIt** plans arm motion to grasp soda.
6.  **Nav2** returns to user.

## Future Directions

- **End-to-End Learning**: Example: Google's RT-2. Inputs Camera + Text -> Outputs Motor Torques directly. No separate modules for mapping or planning.
