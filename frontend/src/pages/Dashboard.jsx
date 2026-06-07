import React from 'react'
import { useNavigate } from 'react-router-dom'
import Navbar from '../components/Navbar'

function Dashboard() {
    const navigate=useNavigate()
    const logout = () => {
        localStorage.removeItem("token");
        navigate("/");
    }
  return (
    <div className="page">
        <Navbar />
        <div className="page-header">
            <h1>Dashboard</h1>
            <p>Choose where you want to continue your preparation</p>
        </div>
        <div className="dashboard-grid">
            <div className="dashboard-card" onClick={()=>{navigate("/Subjects")}}>
                <div className="dashboard-card-icon dashboard-card-icon--subjects">📚</div>
                <h3>Subjects</h3>
                <p>Browse subjects and explore topics for your interview roadmap</p>
            </div>
            <div className="dashboard-card" onClick={() => navigate("/Chat")}>
                <div className="dashboard-card-icon dashboard-card-icon--chat">💬</div>
                <h3>AI Chat</h3>
                <p>Ask questions and get help from your AI interview assistant</p>
            </div>
            <div className="dashboard-card" onClick={logout}>
                <div className="dashboard-card-icon dashboard-card-icon--logout">🚪</div>
                <h3>Logout</h3>
                <p>Sign out of your account securely</p>
            </div>
        </div>
    </div>
  )
}

export default Dashboard
