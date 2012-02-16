%define rname libxml
%define oname %{rname}-ruby
%define name ruby-%{rname}
%define version 1.1.3
%define release %mkrel 3

Summary:	Ruby bindings for libxml2
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://libxml.rubyforge.org/
Source0:	http://rubygems.org/downloads/%{oname}-%{version}.gem
License:	MIT
Group:		Development/Ruby
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	ruby(abi) = 1.8
Requires:	rubygems
BuildRequires:	ruby-devel libxml2-devel rubygems

%description
ruby-libxml provides a clean and fast Ruby interface into the libxml2
library. Can write XML documents and has a friendly interface for
performing XPath queries.

%prep
%setup -q -n %{rname}-%{version}
tar xf data.tar.gz

%build
%gem_build

%install
rm -rf %buildroot
%gem_install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{ruby_sitearchdir}/libxml_ruby.so
