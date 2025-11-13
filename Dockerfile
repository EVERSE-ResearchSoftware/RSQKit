FROM ruby:3.3.7
WORKDIR /usr/src/app
RUN gem install bundler jekyll
COPY Gemfile* ./
RUN bundle install
EXPOSE 4000
