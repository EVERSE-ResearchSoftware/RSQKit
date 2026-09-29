FROM ruby:3.3.7
WORKDIR /usr/src/app
# Necessary to be able to detect remote origin
RUN apt-get update && apt-get install -y git
RUN git config --global --add safe.directory /usr/src/site
RUN gem install bundler jekyll
COPY Gemfile* ./
RUN bundle install
EXPOSE 4000
