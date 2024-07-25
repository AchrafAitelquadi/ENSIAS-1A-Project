import React from 'react';
import { NavLink } from 'react-router-dom';
import './Sidebar.css';
import icons from './importAllSvg';

const Sidebar = () => {
    return (
        <div className="sidebar">
            <div className="logo">
                <img src={icons.ORMVASM} alt="Logo" />
            </div>
            <nav className="menu">
                <ul>
                    <li>
                        <NavLink to="/dashboard" className={({ isActive }) => isActive ? "menu-item active" : "menu-item"}>
                            <img src={icons.dashboard} alt="Dashboard Icon" className="menu-icon" />
                            Dashboard
                        </NavLink>
                    </li>
                    <li>
                        <NavLink to="/agents" className={({ isActive }) => isActive ? "menu-item active" : "menu-item"}>
                            <img src={icons.agents} alt="Agents Icon" className="menu-icon" />    
                            Agents
                        </NavLink>
                    </li>
                    <li>
                        <NavLink to="/services" className={({ isActive }) => isActive ? "menu-item active" : "menu-item"}>
                            <img src={icons.services} alt="Services Icon" className="menu-icon" />
                            Services
                        </NavLink>
                    </li>
                    <li>
                        <NavLink to="/besoins" className={({ isActive }) => isActive ? "menu-item active" : "menu-item"}>
                            <img src={icons.besoins} alt="Besoins Icon" className="menu-icon" />
                            Besoins
                        </NavLink>
                    </li>
                    <li>
                        <NavLink to="/candidatures" className={({ isActive }) => isActive ? "menu-item active" : "menu-item"}>
                            <img src={icons.candidatures} alt="Candidatures Icon" className="menu-icon" />
                            Candidatures
                        </NavLink>
                    </li>
                    <li>
                        <NavLink to="/convocations" className={({ isActive }) => isActive ? "menu-item active" : "menu-item"}>
                            <img src={icons.convocations} alt="Convocations Icon" className="menu-icon" />
                            Convocations
                        </NavLink>
                    </li>
                    <li>
                        <NavLink to="/epreuves" className={({ isActive }) => isActive ? "menu-item active" : "menu-item"}>
                            <img src={icons.calendrier} alt="Calendrier Icon" className="menu-icon" />
                            Calendrier
                        </NavLink>
                    </li>
                    <li>
                        <NavLink to="/chat" className={({ isActive }) => isActive ? "menu-item active" : "menu-item"}>
                            <img src={icons.chat} alt="Chat Icon" className="menu-icon" />
                            Chat
                        </NavLink>
                    </li>
                </ul>
            </nav>
            <div className="footer">
            </div>
        </div>
    );
}

export default Sidebar;
