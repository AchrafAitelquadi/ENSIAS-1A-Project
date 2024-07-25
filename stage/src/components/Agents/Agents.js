// agents.js
import React, { useState } from 'react';
import './Agents.css';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Checkbox, IconButton, Button, TextField } from '@mui/material';
import icons from '../importAllSvg';

const agents = [
  { name: 'Samanta William', code: '#123456789', date: 'March 25, 2021', service: 'Mana William', post: 'Jakarta', grade: 'VII A' },
  { name: 'Tony Soap', code: '#123456789', date: 'March 25, 2021', service: 'James Soap', post: 'Jakarta', grade: 'VII B' },
  { name: 'Karen Hope', code: '#123456789', date: 'March 25, 2021', service: 'Justin Hope', post: 'Jakarta', grade: 'VII C' },
  { name: 'Jordan Nico', code: '#123456789', date: 'March 25, 2021', service: 'Amanda Nico', post: 'Jakarta', grade: 'VII A' },
  { name: 'Nadila Adja', code: '#123456789', date: 'March 25, 2021', service: 'Jack Adja', post: 'Jakarta', grade: 'VII A' },
  { name: 'Johnny Ahmad', code: '#123456789', date: 'March 25, 2021', service: 'Danny Ahmad', post: 'Jakarta', grade: 'VII A' }
];

const Agent = () => {
  const [search, setSearch] = useState('');

  const handleSearchChange = (event) => {
    setSearch(event.target.value);
  };

  const filteredAgents = agents.filter(agent =>
    agent.name.toLowerCase().includes(search.toLowerCase()) ||
    agent.code.toLowerCase().includes(search.toLowerCase()) ||
    agent.service.toLowerCase().includes(search.toLowerCase()) ||
    agent.post.toLowerCase().includes(search.toLowerCase()) ||
    agent.grade.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="agent-container">
      <div className="agent-header">
        <h2>Agents</h2>
        <div className="search-and-button">
          <TextField
            label="Search"
            variant="outlined"
            size="small"
            value={search}
            onChange={handleSearchChange}
            className="search-bar"
          />
          <Button variant="contained" color="primary">+ Ajouter Agent</Button>
        </div>
      </div>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell padding="checkbox">
                <Checkbox />
              </TableCell>
              <TableCell>Name</TableCell>
              <TableCell>Code</TableCell>
              <TableCell>Date Embauche</TableCell>
              <TableCell>Service</TableCell>
              <TableCell>Poste</TableCell>
              <TableCell>Contact</TableCell>
              <TableCell>Grade</TableCell>
              <TableCell>Action</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {filteredAgents.map((agent, index) => (
              <TableRow key={index}>
                <TableCell padding="checkbox">
                  <Checkbox />
                </TableCell>
                <TableCell>{agent.name}</TableCell>
                <TableCell>{agent.code}</TableCell>
                <TableCell>{agent.date}</TableCell>
                <TableCell>{agent.service}</TableCell>
                <TableCell>{agent.post}</TableCell>
                <TableCell>
                  <IconButton><img src={icons.phone} alt="Phone" /></IconButton>
                  <IconButton><img src={icons.email} alt="email" /></IconButton>
                </TableCell>
                <TableCell>{agent.grade}</TableCell>
                <TableCell>
                  <IconButton><img src={icons.more} alt="more" /></IconButton>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
};

export default Agent;
