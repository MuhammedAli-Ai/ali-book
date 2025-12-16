# Project Constitution: Physical AI & Humanoid Robotics Textbook

## Project Identity

**Title:** Hackathon I: Create a Textbook for Teaching Physical AI & Humanoid Robotics Course  
**Organization:** Panaversity  
**Websites:** panaversity.org, ai-native.panaversity.org  
**Timeline:** Submission Deadline - Sunday, Nov 30, 2025 at 06:00 PM

## Vision & Context

### Future of Work
Partnership between people, intelligent agents (AI software), and robots. This shift in human roles is leading to massive demand for new skills.

### Project Goal
Build a portal for authors to create AI-native textbooks and for readers to learn using AI Agents.

## Core Principles

### 1. AI-Native Development
- **Spec-Driven Approach:** All development must follow SpecKit Plus methodology
- **Agent-First:** Leverage Claude Code and AI agents throughout the development process
- **Reusable Intelligence:** Create reusable components via Claude Code Subagents and Agent Skills

### 2. Educational Excellence
- **Comprehensive Coverage:** Cover all aspects of Physical AI and Humanoid Robotics
- **Practical Focus:** Bridge theory with hands-on implementation
- **Accessibility:** Content must be clear for students with varying backgrounds

### 3. Technical Standards

#### Code Quality
- **Clean Architecture:** Separate concerns (frontend, backend, data)
- **Type Safety:** Use TypeScript for frontend, type hints for Python backend
- **Error Handling:** Comprehensive error handling with user-friendly messages
- **Documentation:** Inline comments for complex logic, README for setup

#### Performance
- **Fast Load Times:** Optimize static site generation with Docusaurus
- **Efficient RAG:** Optimize vector search queries in Qdrant
- **Responsive UI:** Ensure smooth experience on all devices

#### Security
- **Environment Variables:** Never commit secrets; use `.env` files
- **Authentication:** Implement secure signup/signin with Better-Auth
- **API Security:** Validate all inputs, implement rate limiting
- **Data Privacy:** Handle user data responsibly

### 4. User Experience

#### Design Principles
- **Premium Aesthetics:** Modern, professional design with glassmorphism effects
- **Dark Theme Focus:** Rich blue dark theme as primary
- **Responsive Design:** Mobile-first approach
- **Accessibility:** WCAG 2.1 AA compliance

#### Interaction Design
- **Intuitive Navigation:** Clear hierarchy and navigation patterns
- **Progressive Enhancement:** Core functionality works without JavaScript
- **Feedback:** Clear loading states and error messages
- **Personalization:** Adapt content based on user background

### 5. Technology Stack

#### Required Tools
- **Development:** Claude Code, Spec-Kit Plus
- **Frontend:** Docusaurus (static site generation)
- **AI/ML:** OpenAI Agents/ChatKit SDKs
- **Backend:** FastAPI (Python)
- **Database:** Neon Serverless Postgres
- **Vector Store:** Qdrant Cloud
- **Authentication:** Better-Auth

#### Development Workflow
1. **Plan:** Create specs and plans using SpecKit Plus
2. **Implement:** Build features incrementally
3. **Test:** Verify functionality before moving forward
4. **Document:** Update documentation as you build
5. **Deploy:** GitHub Pages or Vercel for frontend, cloud hosting for backend

## Project Constraints

### Must Have (Base 100 Points)
1. **AI/Spec-Driven Book Creation:** Complete textbook using Docusaurus, deployed to GitHub Pages
2. **Integrated RAG Chatbot:** Functional chatbot that answers questions based on book content

### Bonus Features (50 Points Each)
1. **Reusable Intelligence:** Claude Code Subagents and Agent Skills
2. **Authentication & Onboarding:** Better-Auth with user background collection
3. **Personalization:** Content adaptation based on user background
4. **Localization:** Urdu translation capability

### Non-Negotiables
- **Public GitHub Repository:** All code must be publicly accessible
- **Live Deployment:** Book must be published and accessible online
- **Demo Video:** Under 90 seconds showcasing key features
- **Deadline:** Sunday, Nov 30, 2025 at 06:00 PM

## Success Metrics

### Technical Metrics
- ✅ Docusaurus build succeeds without errors
- ✅ RAG chatbot responds accurately to book content queries
- ✅ All authentication flows work correctly
- ✅ Site loads in < 3 seconds on 3G connection
- ✅ Mobile responsive on all screen sizes

### Content Metrics
- ✅ All 13 weeks of curriculum covered
- ✅ All 4 major modules documented
- ✅ Hardware requirements clearly specified
- ✅ Code examples included where relevant

### User Experience Metrics
- ✅ Clear navigation structure
- ✅ Professional, modern design
- ✅ Accessible on mobile and desktop
- ✅ Personalization works for logged-in users

## Career Opportunities

Successful completion may lead to:
- Interview to join Panaversity core team
- Potential role as a startup founder
- Teaching opportunities at Panaversity, PIAIC, and GIAIC

## Submission Requirements

**Form URL:** https://forms.gle/CQsSEGM3GeCrL43c8

**Required Items:**
1. Public GitHub Repo Link
2. Published Book Link (GitHub Pages or Vercel)
3. Demo video link (under 90 seconds)
4. WhatsApp number

**Presentation:** Top submissions invited to present via Zoom on Sunday, Nov 30, 2025 starting at 06:00 PM

---

*This constitution serves as the foundation for all project decisions. When in doubt, refer back to these principles.*
