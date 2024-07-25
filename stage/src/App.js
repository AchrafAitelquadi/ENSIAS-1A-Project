import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Dashboard from './components/Dashboard/Dashboard';
import Agents from './components/Agents/Agents';
import './styles.css';

function App() {
    return (
        <Router>
            <div className="app">
                <Sidebar />
                <div className="content">
                    <Routes>
                        <Route path="/" element={<Navigate to="/dashboard" />} />
                        <Route path="/dashboard" element={<Dashboard />} /> 
                        <Route path="/agents" element={<Agents />} />
                    </Routes>
                </div>
            </div>
        </Router>
    );
}

export default App;
