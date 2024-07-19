
document.addEventListener('DOMContentLoaded', () => {
    const homeLink = document.getElementById('home-link');
    const savedLink = document.getElementById('saved-link');
    const newsListSection = document.getElementById('news-list-section');
    const articleSection = document.getElementById('article-section');
    const savedArticlesSection = document.getElementById('saved-articles-section');
    const newsList = document.getElementById('news-list');
    const savedArticlesList = document.getElementById('saved-articles-list');
    const articleContent = document.getElementById('article-content');
    const saveArticleBtn = document.getElementById('save-article-btn');
    const categoryFilter = document.getElementById('category-filter');
    const searchBar = document.querySelector('.search-bar');

    const articles = [
        { id: 1, title: 'Tech News 1', category: 'technology', content: 'Content of Tech News 1' },
        { id: 2, title: 'Sports News 1', category: 'sports', content: 'Content of Sports News 1' },
        { id: 3, title: 'Politics News 1', category: 'politics', content: 'Content of Politics News 1' },
        { id: 4, title: 'Tech News 2', category: 'technology', content: 'Content of Tech News 2' },
    ];

    let savedArticles = [];

    function renderArticles(articlesToRender) {
        newsList.innerHTML = '';
        articlesToRender.forEach(article => {
            const articleElement = document.createElement('div');
            articleElement.classList.add('news-item');
            articleElement.innerText = article.title;
            articleElement.addEventListener('click', () => showArticle(article));
            newsList.appendChild(articleElement);
        });
    }

    function renderSavedArticles() {
        savedArticlesList.innerHTML = '';
        savedArticles.forEach(article => {
            const articleElement = document.createElement('div');
            articleElement.classList.add('news-item');
            articleElement.innerText = article.title;
            articleElement.addEventListener('click', () => showArticle(article));
            savedArticlesList.appendChild(articleElement);
        });
    }

    function showArticle(article) {
        newsListSection.classList.add('hidden');
        savedArticlesSection.classList.add('hidden');
        articleSection.classList.remove('hidden');
        articleContent.innerHTML = `<h1>${article.title}</h1><p>${article.content}</p>`;
        saveArticleBtn.onclick = () => saveArticle(article);
    }

    function saveArticle(article) {
        if (!savedArticles.some(saved => saved.id === article.id)) {
            savedArticles.push(article);
            alert('Article saved!');
        } else {
            alert('Article already saved.');
        }
    }

    homeLink.addEventListener('click', () => {
        newsListSection.classList.remove('hidden');
        articleSection.classList.add('hidden');
        savedArticlesSection.classList.add('hidden');
    });

    savedLink.addEventListener('click', () => {
        newsListSection.classList.add('hidden');
        articleSection.classList.add('hidden');
        savedArticlesSection.classList.remove('hidden');
        renderSavedArticles();
    });

    categoryFilter.addEventListener('change', () => {
        const selectedCategory = categoryFilter.value;
        const filteredArticles = selectedCategory === 'all' ? articles : articles.filter(article => article.category === selectedCategory);
        renderArticles(filteredArticles);
    });

    searchBar.addEventListener('input', () => {
        const keyword = searchBar.value.toLowerCase();
        const filteredArticles = articles.filter(article => article.title.toLowerCase().includes(keyword));
        renderArticles(filteredArticles);
    });

    renderArticles(articles);
});
