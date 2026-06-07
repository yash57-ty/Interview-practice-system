import { React, useState } from 'react'
import api from "../api/axios"
import { useNavigate } from 'react-router-dom'

function Register() {
    const [name, setname] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const navigate = useNavigate()

    const handelRegister = async () => {
        try {
            await api.post('auth/register', {
                name,
                email,
                password
            })
            navigate("/")
        } catch (err) {
            console.error(err)
        }
    }

    return (
        <div className="auth-page">
            <div className="auth-card">
                <div className="auth-logo">
                    <div className="auth-logo-icon">IP</div>
                    <div>
                        <h1>Create account</h1>
                        <p>Join the interview preparation platform</p>
                    </div>
                </div>
                <div className="auth-form">
                    <div className="form-group">
                        <label className="form-label">Name</label>
                        <input className="input" type="text"
                            name="name"
                            value={name}
                            onChange={(e) => { setname(e.target.value) }}
                            placeholder="Enter your name" />
                    </div>
                    <div className="form-group">
                        <label className="form-label">Email</label>
                        <input className="input" type="email"
                            name="email"
                            value={email}
                            onChange={(e) => { setEmail(e.target.value) }}
                            placeholder="Enter your email" />
                    </div>
                    <div className="form-group">
                        <label className="form-label">Password</label>
                        <input className="input" type="password"
                            name="password"
                            value={password}
                            onChange={(e) => { setPassword(e.target.value) }}
                            placeholder="Enter your password" />
                    </div>
                    <button className="btn btn-primary btn-full btn-lg" onClick={handelRegister}>Create Account</button>
                </div>
                <p className="auth-footer">
                    Already have an account?{' '}
                    <span className="auth-link" onClick={() => navigate("/")}>Sign in</span>
                </p>
            </div>
        </div>
    )
}

export default Register
