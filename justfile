default:
    @just --list

# Marketing door (Zola)
site-build:
    cd site && zola build --force

# Documentation door (mdBook)
book-build:
    mdbook build book --dest-dir ../site/static/docs

# Combined: book at /docs, Zola at root
docs-build:
    mdbook build book --dest-dir ../site/static/docs
    cd site && zola build --force
    @echo "output: site/public  (docs at site/public/docs/)"
