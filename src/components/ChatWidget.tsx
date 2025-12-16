import React, { useState, useRef, useEffect } from 'react';
import clsx from 'clsx';
import './ChatWidget.css'; // We'll create this CSS file

interface Message {
  role: 'user' | 'assistant' | 'system';
  content: string;
  sources?: Source[];
}

interface Source {
  title: string;
  url: string;
  snippet: string;
}

export default function ChatWidget() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([
    { role: 'assistant', content: 'Hi! I am the Physical AI course assistant. Ask me anything about the textbook!' }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isOpen]);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMsg: Message = { role: 'user', content: input };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
        // Use localhost for dev, but configurable for prod
        // In real app, use Docusaurus siteConfig to get API URL
        const apiUrl = 'http://localhost:8000/api/chat/query'; 
        
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question: userMsg.content })
        });

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.detail || 'Network response was not ok');
        }

        const data = await response.json();
        
        const assistantMsg: Message = { 
            role: 'assistant', 
            content: data.answer,
            sources: data.sources
        };
        
        setMessages(prev => [...prev, assistantMsg]);
    } catch (error: any) {
        console.error('Chat Error:', error);
        setMessages(prev => [...prev, { role: 'system', content: `Error: ${error.message || 'Could not connect to the brain.'}` }]);
    } finally {
        setLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="chat-widget-container">
      {!isOpen && (
        <button className="chat-widget-toggle" onClick={() => setIsOpen(true)}>
          🤖 Ask AI
        </button>
      )}

      {isOpen && (
        <div className="chat-window">
          <div className="chat-header">
            <h3>Course Assistant</h3>
            <button className="close-btn" onClick={() => setIsOpen(false)}>×</button>
          </div>
          
          <div className="chat-messages">
            {messages.map((msg, idx) => (
              <div key={idx} className={clsx('message', msg.role)}>
                <div className="message-content">
                  {msg.content}
                </div>
                {msg.sources && msg.sources.length > 0 && (
                  <div className="message-sources">
                    <small>Sources:</small>
                    <ul>
                      {msg.sources.map((s, i) => (
                        <li key={i}>
                            <a href={s.url} target="_blank" rel="noopener noreferrer">{s.title}</a>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            ))}
            {loading && <div className="message assistant loading">Thinking...</div>}
            <div ref={messagesEndRef} />
          </div>

          <div className="chat-input-area">
            <textarea 
              value={input} 
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyPress}
              placeholder="Ask a question..."
              rows={1}
            />
            <button onClick={handleSend} disabled={loading}>Send</button>
          </div>
        </div>
      )}
    </div>
  );
}
