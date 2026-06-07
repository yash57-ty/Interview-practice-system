import { useState } from 'react'
import './App.css'
import {BrowserRouter,Routes,Route} from "react-router-dom"
import Login from "./pages/Login"
import Dashboard from "./pages/Dashboard"
import Register from "./pages/Register"
import Subjects from './pages/Subjects'
import Topics from './pages/Topics'
import Roadmap from './pages/Roadmap'
import Chat  from './pages/Chat'
import ProtectedRoute from './components/ProtectedRoute'
function App() {
  return (
   <BrowserRouter>
   <Routes>
    <Route path="/" element={<Login/>}/>
    <Route path="/register" element={<Register/>}/>
    <Route path="/dashboard" element={<ProtectedRoute><Dashboard/></ProtectedRoute>}/>
    <Route path="/Subjects" element={<ProtectedRoute><Subjects/></ProtectedRoute>}/>
    <Route path="/topics/:subjectId" element={<ProtectedRoute><Topics/></ProtectedRoute>}/>
    <Route path="/Roadmap/:subjectId" element={<ProtectedRoute><Roadmap/></ProtectedRoute>}/>
    <Route path="/Chat" element={<ProtectedRoute><Chat/></ProtectedRoute>}/>
   </Routes>
   </BrowserRouter>
  )
}

export default App
