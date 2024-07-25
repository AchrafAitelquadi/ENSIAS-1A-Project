import React from 'react';
import './RightSide.css'; // Ensure this path is correct
import icons from '../importAllSvg'
const agents = [
    { name: 'Samantha William', class: 'Class VII A' },
    { name: 'Tony Soap', class: 'Class VII A' },
    { name: 'Karen Hope', class: 'Class VII A' },
    { name: 'Jordan Nico', class: 'Class VII B' },
    { name: 'Nadila Adja', class: 'Class VII B' },
];

const besoins = [
    { name: 'Samantha William', message: 'Lorem ipsum dolor sit amet...', time: '12:45 PM' },
    { name: 'Tony Soap', message: 'Lorem ipsum dolor sit amet...', time: '12:45 PM' },
    { name: 'Jordan Nico', message: 'Lorem ipsum dolor sit amet...', time: '12:45 PM' },
    { name: 'Nadila Adja', message: 'Lorem ipsum dolor sit amet...', time: '12:45 PM' },
];

const RightSidebar = () => {
    return (
        <div className="right-sidebar">
            <div className="sidebar-content">
            <div className="profile-section">
                <div className="profile-icon agent-avatar">
                    <img src={icons.services} alt="Agent" />
                </div>
                <div className="profile-info">
                    <h4>Prénom Admin</h4>
                    <span>Admin</span>
                </div>
            </div>
            <div className="agents-section">
                <h4>Agents</h4>
                <span>You have 456 students</span>
                <div className="agent-list">
                    {agents.map((agent, index) => (
                        <div key={index} className="agent-item">
                            <div className="agent-avatar">
                                <img src={icons.services} alt="Agent" />
                            </div>
                            <div className="agent-info">
                                <h5>{agent.name}</h5>
                                <span>{agent.class}</span>
                            </div>
                        </div>
                    ))}
                </div>
                <button className="view-more-btn">View More</button>
            </div>
            <div className="besoins-section">
                <h4>Besoins</h4>
                <div className="besoins-list">
                    {besoins.map((besoin, index) => (
                        <div key={index} className="besoin-item">
                            <div className="agent-avatar">
                                <img src={icons.services} alt="Agent" />
                            </div>
                            <div className="besoin-info">
                                <h5>{besoin.name}</h5>
                                <span>{besoin.message}</span>
                            </div>
                            <div className="besoin-time">
                                <span>{besoin.time}</span>
                            </div>
                        </div>
                    ))}
                </div>
                <button className="view-more-btn">View More</button>
            </div>
            </div>
        </div>
    );
}
export default RightSidebar;
