import {React,useState} from 'react'
import api from "../api/axios"
import { Navigate,useNavigate } from 'react-router-dom'
function Login() {
    const [name,setname]=useState("")
    const [password,setPassword]=useState("")
    const navigate=useNavigate()
   const handelLogin= async ()=>{
        try{
            const res=await api.post('auth/login',{
                name,
                password
            })
            localStorage.setItem("token",res.data.access_token)
           navigate("/dashboard")
        }catch(err){
            console.error(err)
        }
   }
  return (
    <div className="auth-page">
        <div className="auth-card">
            <div className="auth-logo">
                <div className="auth-logo-icon">IP</div>
                <div>
                    <h1>Welcome back</h1>
                    <p>Sign in to continue your interview prep</p>
                </div>
            </div>
            <div className="auth-form">
                <div className="form-group">
                    <label className="form-label">Email</label>
                    <input className="input" type="email" 
                    name="Email" 
                    value={name}
                    onChange={(e)=>{setname(e.target.value)}}
                    placeholder="Enter your email"/>
                </div>
                <div className="form-group">
                    <label className="form-label">Password</label>
                    <input className="input" type="password"
                    name="password"
                    value={password} 
                    onChange={(e)=>{setPassword(e.target.value)}}
                    placeholder="Enter your password"/>
                </div>
                <button className="btn btn-primary btn-full btn-lg" onClick={handelLogin}>Sign In</button>
            </div>
            <p className="auth-footer">
                Don't have an account?{' '}
                <span className="auth-link" onClick={() => navigate("/register")}>Create one</span>
            </p>
        </div>
    </div>
  )
}

export default Login
