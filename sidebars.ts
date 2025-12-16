import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  textbookSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Module 1: Intro to Physical AI',
      collapsible: true,
      collapsed: false,
      items: [
        'week-01-02/introduction-to-physical-ai',
        'week-01-02/sensor-systems',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: ROS 2 Fundamentals',
      collapsible: true,
      collapsed: true,
      items: [
        'week-03-05/ros2-architecture',
        'week-03-05/nodes-and-topics',
        'week-03-05/python-packages',
      ],
    },
    {
      type: 'category',
      label: 'Module 3: Robot Simulation',
      collapsible: true,
      collapsed: true,
      items: [
        'week-06-07/gazebo-setup',
        'week-06-07/urdf-sdf',
        'week-06-07/unity-visualization',
      ],
    },
    {
      type: 'category',
      label: 'Module 4: NVIDIA Isaac Platform',
      collapsible: true,
      collapsed: true,
      items: [
        'week-08-10/isaac-sdk',
        'week-08-10/reinforcement-learning',
        'week-08-10/sim-to-real',
      ],
    },
    {
      type: 'category',
      label: 'Module 5: Humanoid Development',
      collapsible: true,
      collapsed: true,
      items: [
        'week-11-12/bipedal-locomotion',
        'week-11-12/manipulation',
        'week-11-12/interaction-design',
      ],
    },
    {
      type: 'category',
      label: 'Module 6: Conversational Robotics',
      collapsible: true,
      collapsed: true,
      items: [
        'week-13/conversational-robotics',
        'week-13/multimodal-interaction',
      ],
    },
  ],
};

export default sidebars;
