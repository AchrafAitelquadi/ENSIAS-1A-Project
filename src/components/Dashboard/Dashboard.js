import React, { useState } from 'react';
import './Dashboard.css';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, BarChart, Bar, PieChart, Pie, Cell } from 'recharts';
import { Calendar, Input } from 'antd'; // Import the Input component from Ant Design
import { FileDoneOutlined } from '@ant-design/icons';
import icons from '../importAllSvg';
import { scaleSequential } from 'd3-scale';
import { interpolateRainbow } from 'd3-scale-chromatic';
import RightSide from './RightSide';

const getColor = (index, total) => {
    const colorScale = scaleSequential(interpolateRainbow).domain([0, total]);
    return colorScale(index);
};

const lineChartData = [
    { name: 'Jan', thisWeek: 40, lastWeek: 24 },
    { name: 'Feb', thisWeek: 30, lastWeek: 14 },
    { name: 'Mar', thisWeek: 20, lastWeek: 98 },
    { name: 'Apr', thisWeek: 27, lastWeek: 39 },
    { name: 'May', thisWeek: 18, lastWeek: 48 },
    { name: 'Jun', thisWeek: 23, lastWeek: 38 },
    { name: 'Jul', thisWeek: 34, lastWeek: 43 },
];

const barChartData = [
    { name: 'Mon', thisWeek: 40, lastWeek: 24 },
    { name: 'Tue', thisWeek: 30, lastWeek: 13 },
    { name: 'Wed', thisWeek: 20, lastWeek: 98 },
    { name: 'Thu', thisWeek: 27, lastWeek: 39 },
    { name: 'Fri', thisWeek: 18, lastWeek: 48 },
    { name: 'Sat', thisWeek: 23, lastWeek: 38 },
    { name: 'Sun', thisWeek: 34, lastWeek: 43 },
];

const barChartDataSpecialite = [
    { name: 'Droit', value: 3 },
    { name: 'Technicien informatique', value: 2 },
    { name: 'Wed', value: 7 },
    { name: 'Thu', value: 5 },
    { name: 'Fri', value: 4 },
    { name: 'Sat', value: 8 },
    { name: 'Sun', value: 4 },
];

const COLORS = ['#26815F', '#FF715B'];

const pieChartData = [
    { name: 'F', value: 1245 },
    { name: 'M', value: 1356 },
];

const Dashboard = () => {
    const [searchTerm, setSearchTerm] = useState("");

    const handleSearch = (e) => {
        setSearchTerm(e.target.value);
    };

    return (
    <div className='dashboard-container'>
        <div className="dashboard">
            <div className="dashboard-header">
                <div className="dashboard-title">Dashboard</div>
                <Input
                    className="search-bar"
                    placeholder="Search..."
                    value={searchTerm}
                    onChange={handleSearch}
                />
            </div>
            <div className="stats-cards">
                <div className="card combined-card">
                    <div className="card-section">
                        <img src={icons.agents} alt="Employee Icon" className="card-icon" />
                        <div>
                            <h3>Employés</h3>
                            <p>932</p>
                        </div>
                    </div>
                    <div className="card-section">
                        <img src={icons.services} alt="Service Icon" className="card-icon card-icon-services" />
                        <div>
                            <h3>Services</h3>
                            <p>754</p>
                        </div>
                    </div>
                </div>
                <div className="card candidature-card">
                    <FileDoneOutlined className="card-icon" />
                    <div className="candidature-content">
                        <h3>Candidatures</h3>
                        <p>754</p>
                    </div>
                </div>
                <div className="button-group">
                    <div className="button creer-avis">+ Créer Avis</div>
                    <div className="button creer-epreuve">+ Créer Epreuve</div>
                </div>
            </div>
            <div className="candidature-chart-container">
                <h3 className="chart-title">Nombre Candidatures</h3>
                <ResponsiveContainer width="100%" height={300}>
                    <LineChart data={lineChartData}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="name" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Line type="monotone" dataKey="thisWeek" stroke="#ff7300" />
                        <Line type="monotone" dataKey="lastWeek" stroke="#387908" />
                    </LineChart>
                </ResponsiveContainer>
            </div>
            <div className="chart-container">
                <div className="calendrier-container">
                    <h3 className="chart-title">Calendrier Recrutement</h3>
                    <Calendar fullscreen={false} />
                </div>  
                <div className="besoins-chart-container">
                    <h3 className="chart-title">Besoins</h3>
                    <ResponsiveContainer width="105%" height={350}>
                        <BarChart data={barChartData}>
                            <CartesianGrid strokeDasharray="3 3" />
                            <XAxis dataKey="name" />
                            <YAxis />
                            <Tooltip />
                            <Legend />
                            <Bar dataKey="thisWeek" fill="#8884d8" />
                            <Bar dataKey="lastWeek" fill="#82ca9d" />
                        </BarChart>
                    </ResponsiveContainer>
                </div>
            </div>
            <div className="candidature-chart-container">
                <h3 className="chart-title">Pourcentages de candidatures par spécialité</h3>
                <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={barChartDataSpecialite} layout="vertical" margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis type="number" />
                        <YAxis dataKey="name" type="category" />
                        <Tooltip />
                        <Bar dataKey="value">
                        {barChartDataSpecialite.map((entry, index) => (
                            <Cell key={`cell-${index}`} fill={getColor(index, barChartDataSpecialite.length)} />
                        ))}
                    </Bar>
                    </BarChart>
                </ResponsiveContainer>
            </div>
            <div className="donut-chart-container">
                <h3 className="chart-title">Candidats</h3>
                <div className="donut-chart-legend">
                    <div className="legend-item">
                        <span className="legend-color" style={{ backgroundColor: COLORS[0] }}></span>
                        F <span className="legend-value">1.245</span>
                    </div>
                    <div className="legend-item">
                        <span className="legend-color" style={{ backgroundColor: COLORS[1] }}></span>
                        M <span className="legend-value">1.356</span>
                    </div>

                </div>
                <ResponsiveContainer width="100%" height={200}>
                    <PieChart>
                        <Pie
                            data={pieChartData}
                            cx="50%"
                            cy="50%"
                            innerRadius={60}
                            outerRadius={80}
                            fill="#8884d8"
                            paddingAngle={5}
                            dataKey="value"
                        >
                            {pieChartData.map((entry, index) => (
                                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                            ))}
                        </Pie>
                    </PieChart>
                </ResponsiveContainer>
            </div>
            
                <RightSide/>
        </div>
    </div>
    );
}

export default Dashboard;
