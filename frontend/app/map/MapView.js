"use client";

import { useEffect, useState } from "react";
import dynamic from "next/dynamic";

const Map = dynamic(() => import("react-leaflet").then(mod => mod.MapContainer), { ssr: false });
const Tile = dynamic(() => import("react-leaflet").then(mod => mod.TileLayer), { ssr: false });
const Marker = dynamic(() => import("react-leaflet").then(mod => mod.Marker), { ssr: false });
const Popup = dynamic(() => import("react-leaflet").then(mod => mod.Popup), { ssr: false });

export default function MapView() {
  const [reports,setReports] = useState([]);
  useEffect(()=>{ fetch("http://localhost:8000/dashboard/summary").then(r=>r.json()).then(setReports)},[]);
  const categoryColors = {"Flood":"blue","Fire":"red","Earthquake":"orange","Medical Emergency":"green","Food/Water Shortage":"teal","Power Outage":"yellow","Road Block":"purple","Building Collapse":"brown","Security/Violence":"black","Other":"gray"};
  return <Map center={[24.8607,67.0011]} zoom={12} style={{height:"100vh",width:"100%"}}>
    <Tile url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/>
    {reports.map(r=><Marker key={r.id} position={[r.lat,r.lon]}>
      <Popup>
        <b>{r.category}</b><br/>{r.description}<br/>Reliability: {r.reliability}%<br/>Confirmed by {r.merged_count} report(s)<br/>Explanation: {r.ai_explanation}
      </Popup>
    </Marker>)}
  </Map>
}
