# Generated from libxml-ruby-1.1.3.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	libxml-ruby

Summary:	Ruby libxml bindings
Name:		rubygem-%{rbname}

Version:	1.1.3
Release:	3
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://libxml.rubyforge.org/
Source0:	%{rbname}-%{version}.gem
Patch0:		libxml-ruby-1.1.3-ruby1.9.patch
BuildRequires:	rubygems 
BuildRequires:	ruby-devel libxml2-devel
%rename		ruby-libxml

%description
The Libxml-Ruby project provides Ruby language bindings for the GNOME Libxml2
XML toolkit. It is free software, released under the MIT License.
Libxml-ruby's primary advantage over REXML is performance - if speed  is your
need, these are good libraries to consider, as demonstrated by the informal
benchmark below.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q
%patch0 -p1 -b .ruby19~

%build
%gem_build

%check
rake test

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/libxml
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/libxml/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/xml
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/xml/*.rb
%{ruby_sitearchdir}/libxml.so
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*
