import React, { useEffect, useState } from 'react'
import api from "../api/axios"
import { Navigate,useNavigate } from 'react-router-dom'
import Navbar from '../components/Navbar'

function Subjects() {
    const [Subjects,setSubjects]=useState([])
    const navigate=useNavigate()
    useEffect(()=>{
        async function fetchSubject(){
            try{
                const res=await api.get("/subjects")
                setSubjects(res.data)
            }catch(err){
                console.error(err)
            }
        }
        fetchSubject()
    },[])
  return (
    <div className="page">
        <Navbar />
        <div className="page-header">
            <h1>Subjects</h1>
            <p>Select a subject to view its topics and generate your roadmap</p>
        </div>
        <div className="subject-grid">
        {
            Subjects.map((subject)=>{
                return(
                    <div className="subject-card" key={subject.id} 
                        onClick={()=>{navigate(`/topics/${subject.id}`)}}>
                        <h3>{subject.name}</h3>
                        {subject.description && <p>{subject.description}</p>}
                        <div className="subject-card-arrow">View topics →</div>
                    </div>
                )
            })
        }
        </div>
        {Subjects.length === 0 && (
            <div className="empty-state">No subjects available yet.</div>
        )}
    </div>
  )
}

export default Subjects
