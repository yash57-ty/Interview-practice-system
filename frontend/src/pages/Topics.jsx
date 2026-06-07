import React, { useState } from "react";
import { useEffect } from "react";
import api from "../api/axios"
import { useParams ,useNavigate, Outlet} from "react-router-dom";
import Navbar from '../components/Navbar'

function Topics(){  
    const [Topics,setTopics]=useState([])
    const {subjectId}=useParams()
    const navigate=useNavigate()
    useEffect(()=>{
        async function fetchtopics(){
            try{
                const res=await api.get(`/topics/subject/${subjectId}`)
                setTopics(res.data)
            }catch(err){
                console.error(err)
            }
        }
        fetchtopics()
    },[])

    async function generateRoadmap(){
        try{
           const token=localStorage.getItem("token")
            await api.post(
                "/roadmaps/generate",{
                    subject_id: subjectId
                },{
                    headers: {
                    Authorization: `Bearer ${token}`
                    }
                }
                );
            navigate(`/Roadmap/${subjectId}`)
        }catch(err){
            console.error(err)
        }
    }
    return(
        <div className="page">
        <Navbar />
        <div className="page-header">
            <h1>Topics</h1>
            <p>Click any topic to start learning with AI, or generate your study roadmap below</p>
        </div>
        <div className="topic-list">
        {
            Topics.map((topic, index)=>{
                return(
                    <div className="topic-card topic-card--clickable" key={topic.id}
                        onClick={() => navigate("/Chat", { state: { topicName: topic.name, topicDescription: topic.description } })}>
                        <div className="topic-number">{index + 1}</div>
                        <div>
                            <h3>{topic.name}</h3>
                            {topic.description && <p>{topic.description}</p>}
                            <div className="subject-card-arrow">Start learning →</div>
                        </div>
                    </div>
                )
            })
        }
        </div>

        {Topics.length === 0 && (
            <div className="empty-state">No topics found for this subject.</div>
        )}

        <div className="topic-actions">
            <button className="btn btn-primary btn-lg" onClick={generateRoadmap}
            >Generate Roadmap</button>
        </div>
        <Outlet/>
        </div>
    )
}

export default Topics
