import React from 'react'
import { useNavigate } from 'react-router-dom'

function Navbar() {
    const navigate = useNavigate()

    const logout = () => {
        localStorage.removeItem("token");
        navigate("/");
    }

    return (
        <nav className="navbar">
            <a className="navbar-brand" href="/dashboard" onClick={(e) => { e.preventDefault(); navigate("/dashboard"); }}>
                <span className="navbar-brand-icon">IP</span>
                Interview Prep
            </a>
            <div className="navbar-links">
                <button className="nav-link" onClick={() => navigate("/dashboard")}>Dashboard</button>
                <button className="nav-link" onClick={() => navigate("/Subjects")}>Subjects</button>
                <button className="nav-link" onClick={() => navigate("/Chat")}>AI Chat</button>
                <button className="nav-link nav-link--logout" onClick={logout}>Logout</button>
            </div>
        </nav>
    )
}

export default Navbar
