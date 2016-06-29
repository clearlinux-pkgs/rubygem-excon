#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-excon
Version  : 0.50.1
Release  : 7
URL      : https://rubygems.org/downloads/excon-0.50.1.gem
Source0  : https://rubygems.org/downloads/excon-0.50.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-activesupport
BuildRequires : rubygem-bundler
BuildRequires : rubygem-delorean
BuildRequires : rubygem-eventmachine
BuildRequires : rubygem-json
BuildRequires : rubygem-open4
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-shindo
BuildRequires : rubygem-sinatra

%description
# excon
Usable, fast, simple Ruby HTTP 1.1
Excon was designed to be simple, fast and performant. It works great as a general HTTP(s) client and is particularly well suited to usage in API clients.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n excon-0.50.1
gem spec %{SOURCE0} -l --ruby > rubygem-excon.gemspec

%build
export LANG=C
gem build rubygem-excon.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
excon-0.50.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/excon-0.50.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/CONTRIBUTORS.md
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/Gemfile.lock
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/LICENSE.md
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/class_vs_lambda.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/concat_vs_insert.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/concat_vs_interpolate.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/cr_lf.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/downcase-eq-eq_vs_casecmp.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/excon.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/excon_vs.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/for_vs_array_each.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/for_vs_hash_each.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/has_key-vs-lookup.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/headers_case_sensitivity.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/headers_split_vs_match.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/implicit_block-vs-explicit_block.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/merging.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/single_vs_double_quotes.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/string_ranged_index.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/strip_newline.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/benchmarks/vs_stdlib.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/changelog.txt
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/data/cacert.pem
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/excon.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/connection.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/constants.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/error.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/extensions/uri.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/headers.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/middlewares/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/middlewares/capture_cookies.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/middlewares/decompress.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/middlewares/escape_path.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/middlewares/expects.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/middlewares/idempotent.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/middlewares/instrumentor.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/middlewares/mock.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/middlewares/redirect_follower.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/middlewares/response_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/pretty_printer.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/response.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/socket.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/ssl_socket.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/standard_instrumentor.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/unix_socket.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/lib/excon/utils.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/authorization_header_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/bad_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/basic_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/complete_responses.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/data/127.0.0.1.cert.crt
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/data/127.0.0.1.cert.key
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/data/excon.cert.crt
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/data/excon.cert.key
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/data/xs
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/error_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/header_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/middlewares/canned_response_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/middlewares/capture_cookies_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/middlewares/decompress_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/middlewares/escape_path_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/middlewares/idempotent_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/middlewares/instrumentation_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/middlewares/mock_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/middlewares/redirect_follower_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/pipeline_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/proxy_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/query_string_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/basic.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/basic.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/basic_auth.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/deflater.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/proxy.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/query_string.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/redirecting.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/redirecting_with_cookie.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/request_headers.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/request_methods.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/response_header.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/ssl.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/ssl_mismatched_cn.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/ssl_verify_peer.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/streaming.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/thread_safety.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/timeout.ru
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/rackups/webrick_patch.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/request_headers_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/request_method_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/request_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/response_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/servers/bad.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/servers/eof.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/servers/error.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/servers/good.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/thread_safety_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/timeout_tests.rb
/usr/lib64/ruby/gems/2.3.0/gems/excon-0.50.1/tests/utils_tests.rb
/usr/lib64/ruby/gems/2.3.0/specifications/excon-0.50.1.gemspec
