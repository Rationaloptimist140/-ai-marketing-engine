const metrics = [
  { label: "Affiliate revenue", value: "£0.00", note: "No conversions recorded yet" },
  { label: "Agency recurring revenue", value: "£0.00", note: "No active clients yet" },
  { label: "Active campaigns", value: "0", note: "Create your first campaign" },
  { label: "Pending approvals", value: "0", note: "Human approval is required" },
];
const agents = ["Market intelligence", "Affiliate opportunity", "Marketing strategy", "Content production", "Creative direction", "Compliance review", "Growth analytics", "Client acquisition"];
export default function Home() {
  return <main className="shell">
    <header><span className="pill">MVP foundation · Development</span><h1>AI Marketing Engine</h1><p className="muted">One workspace for affiliate growth and client advertising operations.</p></header>
    <nav className="nav">{["Overview", "Campaigns", "AI workforce", "Clients", "Affiliates", "Approvals", "Analytics", "Settings"].map(x=><span key={x}>{x}</span>)}</nav>
    <section className="grid">{metrics.map(x=><article className="panel" key={x.label}><div className="muted">{x.label}</div><div className="stat">{x.value}</div><small className="muted">{x.note}</small></article>)}</section>
    <section style={{marginTop:28}}><h2>AI workforce</h2><div className="grid">{agents.map((x,i)=><article className="panel" key={x}><strong>{String(i+1).padStart(2,"0")} · {x}</strong><p className="muted">Registered · Execution adapter pending</p></article>)}</div></section>
    <section style={{marginTop:28}} className="panel"><h2>Next step</h2><p className="muted">Connect the backend API, then create your first internal workspace and campaign. Publishing and advertising actions remain disabled until explicit human approval and verified integrations are implemented.</p></section>
  </main>;
}
