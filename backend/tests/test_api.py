def test_health(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200 and response.json()["status"] == "ok"
def test_agent_registry_has_eight_agents(client):
    response = client.get("/api/v1/agents")
    assert response.status_code == 200 and len(response.json()) == 8
def test_workspace_and_campaign_flow(client):
    w = client.post("/api/v1/workspaces", json={"name": "Internal", "workspace_type": "internal"}); assert w.status_code == 201
    wid = w.json()["id"]
    c = client.post(f"/api/v1/workspaces/{wid}/campaigns", json={"name": "AI software launch", "objective": "affiliate", "channels": ["x", "blog"]})
    assert c.status_code == 201 and c.json()["workspace_id"] == wid and c.json()["status"] == "draft"
def test_campaign_cannot_be_queued_under_wrong_workspace(client):
    a = client.post("/api/v1/workspaces", json={"name": "Workspace One"}).json()
    b = client.post("/api/v1/workspaces", json={"name": "Workspace Two"}).json()
    c = client.post(f"/api/v1/workspaces/{a['id']}/campaigns", json={"name": "Campaign", "objective": "agency"}).json()
    r = client.post(f"/api/v1/workspaces/{b['id']}/campaigns/{c['id']}/agent-runs?agent_name=content")
    assert r.status_code == 404
