import React from 'react'
import { useEffect,useState} from 'react'
import {useParams} from 'react-router-dom'
import api from '../api/axios'
import Navbar from '../components/Navbar'

function Roadmap() {
    const [roadmaps,setroadmaps]=useState([])
    const {subjectId}=useParams()
    useEffect(()=>{

        async function fetchroadmaps(){
            const token=localStorage.getItem("token")
            try{
                const res=await api.get(`/roadmaps/${subjectId}`,{
                    headers:{
                        Authorization:`Bearer ${token}`
                    }
                })
                console.log(res.data)
                setroadmaps(res.data)
            }catch(err){
                console.error(err)
            }
        }
        fetchroadmaps()
    },[])
  return (
    <div className="page">
    <Navbar />
    <div className="page-header">
      <h1>Study Roadmap</h1>
      <p>Your week-by-week plan to master this subject</p>
    </div>
    {roadmaps.length > 0 ? (
      <div className="roadmap-timeline">
      {roadmaps.map((item) => (
        <div className="roadmap-item" key={item.id}>
          <div className="roadmap-week-badge">W{item.week}</div>
          <div className="roadmap-content">
            <h3>{item.title}</h3>
            {item.description && <p>{item.description}</p>}
          </div>
        </div>
      ))}
      </div>
    ) : (
      <div className="roadmap-empty">
        <p>No roadmap generated yet. Go back to topics and click "Generate Roadmap".</p>
      </div>
    )}
    </div>
  )
}

export default Roadmap
