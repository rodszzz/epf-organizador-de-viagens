% rebase('layout.tpl', title='Dashboard')

<style>
    .welcome-header {
        margin-bottom: 2rem;
    }
    .dashboard-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
    }
    .card-link {
        text-decoration: none;
        color: inherit;
    }
    .dashboard-card {
        border-radius: 8px;
        padding: 2rem;
        text-align: center;
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        border: 1px solid #dbdbdb;
    }
    .dashboard-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }
    .card-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
    }
</style>

<div class="container">
    <div class="welcome-header">
        <h1 class="title">Bem-vindo, {{user_name}}!</h1>
        <h2 class="subtitle">O que gostaria de fazer hoje?</h2>
    </div>

    <div class="dashboard-grid">
        <a href="/search" class="card-link">
            <div class="dashboard-card has-background-info-light">
                <div class="card-icon">✈️</div>
                <h3 class="title is-4">Buscar Novos Voos</h3>
                <p>Encontre as melhores ofertas para a sua próxima viagem.</p>
            </div>
        </a>

        <a href="/trips" class="card-link">
            <div class="dashboard-card has-background-success-light">
                <div class="card-icon">🧳</div>
                <h3 class="title is-4">Minhas Viagens</h3>
                <p>Veja as viagens que você já reservou e guardou.</p>
            </div>
        </a>
        <a href="/account" class="card-link"> <div class="dashboard-card has-background-warning-light">
                <div class="card-icon">👤</div>
                <h3 class="title is-4">Minha Conta</h3>
                <p>Atualize as suas informações pessoais e de login.</p>
            </div>
        </a>
        </a>
    </div>
</div>
